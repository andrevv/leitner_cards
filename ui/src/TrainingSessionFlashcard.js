import { useState } from "react"

export default function TrainingSessionFlashcard(props) {
	const [answer, setAnswer] = useState('')
	const [correct, setCorrect] = useState(false)

	return (
		<>
			<div className="m-2 p-2 border rounded shadow">
				{ correct &&
					<div>Correct!</div>
				}
				<label className="block">
					<span>{props.question}</span>
				</label>
				<label className="block">
					<input type="text" id="answer" className="m-1 block w-2/4" onChange={e => setAnswer(e.target.value)} value={answer} />
				</label>
				<button
					className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
					onClick={() => checkAnswer(answer)}>
						Answer
				</button>
			</div>
		</>
	)

	function checkAnswer(answer) {
		setCorrect(answer === props.answer)
	}
}
