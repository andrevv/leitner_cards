import { useEffect, useState } from 'react'
import TrainingSessionFlashcard from './TrainingSessionFlashcard'

function TrainingSession() {
	const [flashcards, setFlashcards] = useState([])
	const [session, setSession] = useState()

	useEffect(() => {
		fetch('http://localhost:5000/api/training', {
			method: 'GET',
		})
			.then(resp => resp.json())
			.then(data => {
				setSession(data)
			})
	}, [])

	return (
		<>
			{
				!session &&
					<button
						className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
						onClick={() => createSession()}>
							Create session
					</button>
			}
			{
				session &&
				<div className="flex flex-wrap">
					{session.flashcards.map(flashcard => <TrainingSessionFlashcard key={flashcard.flashcard.id} question={flashcard.flashcard.question} answer={flashcard.flashcard.answer} />)}
				</div>
			}
		</>
	)

	function createSession() {
		fetch('http://localhost:5000/api/training', {
				method: 'POST'
			})
			.then(resp => resp.json())
			.then(data => {
				setSession(data)
			})
	}
}

export default TrainingSession
