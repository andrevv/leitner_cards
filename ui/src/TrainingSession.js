import { useEffect, useState } from 'react'
import TrainingSessionFlashcard from './TrainingSessionFlashcard'

function TrainingSession() {
	const [session, setSession] = useState()
	const [flashcardIndex, setFlashcardIndex] = useState(0)

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
				<button
					className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
					onClick={() => deleteSession(session.id)}>
						Delete session
				</button>
			}
			{
				session &&
				<TrainingSessionFlashcard
					flashcard={session.flashcards[flashcardIndex].flashcard}
					sessionId={session.id}
					onCorrectAnswer={handleCorrectAnswer} />
			}
		</>
	)

	function createSession() {
		fetch('http://localhost:5000/api/training/sessions', {
				method: 'POST'
			})
			.then(resp => resp.json())
			.then(data => {
				setSession(data)
			})
	}

	function deleteSession(id) {
		fetch(`http://localhost:5000/api/training/${id}`, {
				method: 'DELETE'
			})
			.then(() => {
				setSession(null)
			})
	}

	function handleCorrectAnswer() {
		setFlashcardIndex(curr => curr + 1)
	}
}

export default TrainingSession
