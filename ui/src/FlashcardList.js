import { useEffect, useState } from 'react';
import './App.css'
import './Flashcard'
import Flashcard from './Flashcard';

function FlashcardList() {
  const [flashcards, setFlashcards] = useState([])
  const [question, setQuestion] = useState()
  const [answer, setAnswer] = useState()
  
  useEffect(() => {
    fetch('http://localhost:5000/api/flashcards')
      .then(resp => resp.json())
      .then(data => setFlashcards(data))
  }, [])

  return (
		<>
			<div className="my-4">  
				<label className="block">
					<span className="text-gray-700">Question: </span>
					<input type="text" id="question" className="m-1 block w-2/4" onChange={e => setQuestion(e.target.value)} value={question} />
				</label>
				<label className="block">
					<span className="text-gray-700">Answer: </span>
					<input type="text" id="answer" className="m-1 block w-2/4" onChange={e => setAnswer(e.target.value)} value={answer} />
				</label>
				<button
					className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
					onClick={() => addFlashcard(question, answer)}>
						Add a Flashcard
				</button>
			</div>
			<div className="flex flex-wrap">
				{flashcards.map(flashcard =>
					<Flashcard
						key={flashcard.id}
						question={flashcard.question}
						answer={flashcard.answer} />)}
			</div>
		</>
  )

  function addFlashcard(question, answer) {
    fetch('http://localhost:5000/api/flashcards', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        question: question,
        answer: answer
      })
    })
    .then(() => {
      fetch('http://localhost:5000/api/flashcards')
        .then(resp => resp.json())
        .then(data => {
          setFlashcards(data)
          setQuestion('')
          setAnswer('')
        })
    })
  }
}

export default FlashcardList
