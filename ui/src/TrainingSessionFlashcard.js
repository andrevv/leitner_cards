import { useState } from "react"

export default function TrainingSessionFlashcard(props) {
	const [answer, setAnswer] = useState('')
	const [correct, setCorrect] = useState(false)

	return (
		<>
			<div className="m-2 p-2 border rounded shadow w-1/2 mx-auto">
				{ correct &&
					<div>Correct!</div>
				}
				<label className="block">
					<span className="w-full text-center">{props.flashcard.question}</span>
				</label>
				<label className="block">
					<input type="text" id="answer" className="m-1 block w-full" onChange={e => setAnswer(e.target.value)} value={answer} />
				</label>
				<button
					className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
					onClick={() => sendAnswer(answer)}>
						Answer
				</button>
			</div>
		</>
	)

	function sendAnswer(answer) {
		fetch(`http://localhost:5000/api/training/sessions/${props.sessionId}/flashcards/${props.flashcard.id}/answer`, {
			method: 'POST',
			headers: {
        'Content-Type': 'application/json'
      },
			body: JSON.stringify({
				answer: answer
			})
		})
		.then(resp => resp.text())
		.then(data => console.log(data))
	}
}
