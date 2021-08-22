function Flashcard(props) {
	return (
		<div className="m-2 p-2 border rounded shadow">
			<h1>{props.question}</h1>
			<h2>{props.answer}</h2>
		</div>
	)
}

export default Flashcard
