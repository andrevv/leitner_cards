function Flashcard(props) {
	return (
		<div className="ml-2 mr-2 p-5 border rounded shadow">
			<h1>Q: {props.question}</h1>
			<h2>A: {props.answer}</h2>
		</div>
	)
}

export default Flashcard
