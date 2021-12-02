import {useEffect, useState} from "react";

function PracticeFlashcard(props) {
    const [question, setQuestion] = useState(props.question)
    const [userAnswer, setUserAnswer] = useState('')
    const [isWrongAnswer, setIsWrongAnswer] = useState(false)
    const [correctAnswer, setCorrectAnswer] = useState('')

    return (
        <>
            <div className={'p-5 border rounded shadow'}>
                <h1 className={'text-center'}>{props.flashcard.question}</h1>
                {
                    !isWrongAnswer &&
                    <div>
                        <input
                            type="text"
                            className={'mt-3 rounded w-full'}
                            value={userAnswer}
                            onChange={e => setUserAnswer(e.target.value)}/>
                        <div className={'mt-3 flex gap-2'}>
                            <button
                                className={'border rounded-lg shadow p-3 hover:bg-gray-100'}
                                onClick={() => attempt(props.flashcard, userAnswer)}>
                                Show answer
                            </button>
                            <button
                                className={'border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white'}
                                onClick={() => attempt(props.flashcard, userAnswer)}>
                                Check answer
                            </button>
                        </div>
                    </div>
                }
                {
                    isWrongAnswer &&
                    <div>
                        <div className={'line-through text-red-500 text-center'}>{userAnswer}</div>
                        <div className={'text-center'}>{correctAnswer}</div>
                        <button
                            className={'border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white w-full'}
                            onClick={() => onAnswer()}>
                            Next
                        </button>
                    </div>
                }
            </div>
        </>
    )

    function onAnswer() {
        setUserAnswer(null)
        setCorrectAnswer(null)
        setIsWrongAnswer(false)
        props.onAnswer()
    }

    function attempt(flashcard, answer) {
        fetch(`/api/flashcards/${flashcard.id}/attempt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answer: answer
            })
        })
            .then(resp => resp.json())
            .then(data => {
                if (data.is_correct) {
                    onAnswer()
                    return
                }

                setIsWrongAnswer(true)
                setCorrectAnswer(data.answer)
            })
    }
}

export default PracticeFlashcard
