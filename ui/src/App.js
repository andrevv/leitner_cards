import { useEffect, useState } from 'react';
import './App.css'
import './Flashcard'
import Flashcard from './Flashcard';

function App() {
  const [flashcards, setFlashcards] = useState([])
  useEffect(() => {
    fetch('http://localhost:5000/api/flashcards')
      .then(resp => resp.json())
      .then(data => setFlashcards(data))
  }, [])
  return (
    <div className="container mx-auto">
      <div className="flex">
        {flashcards.map(flashcard =>
          <Flashcard
          key={flashcard.id}
          question={flashcard.question}
          answer={flashcard.answer} />)}
      </div>
    </div>
  )
}

export default App
