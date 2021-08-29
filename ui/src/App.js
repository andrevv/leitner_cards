import { useEffect, useState } from 'react';
import './App.css'
import './Flashcard'
import Flashcard from './Flashcard';

function App() {
  const [flashcards, setFlashcards] = useState([])
  const [question, setQuestion] = useState()
  const [answer, setAnswer] = useState()
  useEffect(() => {
    fetch('http://localhost:5000/api/flashcards')
      .then(resp => resp.json())
      .then(data => setFlashcards(data))
  }, [])
  return (
    <div className="container mx-auto">
      <fieldset className="my-1">
        <label htmlFor="question">Question: </label>
        <input type="text" id="question" className="border rounded" onChange={e => setQuestion(e.target.value)} />
      </fieldset>
      <fieldset className="my-1">
        <label htmlFor="answer">Answer: </label>
        <input type="text" id="answer" className="border rounded" onChange={e => setAnswer(e.target.value)} />
      </fieldset>
      <button
        className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white"
        onClick={() => addFlashcard(question, answer)}>
          Add a Flashcard
      </button>
      <div className="flex">
        {flashcards.map(flashcard =>
          <Flashcard
          key={flashcard.id}
          question={flashcard.question}
          answer={flashcard.answer} />)}
      </div>
    </div>
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
        .then(data => setFlashcards(data))
    })
  }
}

export default App
