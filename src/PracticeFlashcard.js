import {useEffect, useState} from "react";

function PracticeFlashcard(props) {
    const [answer, setAnswer] = useState('')

    useEffect(() => {
        setAnswer('')
    }, [answer])

    return (
        <>
            <div className={'p-5 border rounded shadow'}>
                <h1 className={'text-center'}>{props.flashcard.question}</h1>
                <input
                    type="text"
                    className={'mt-3 rounded w-full'}
                    value={answer}
                    onChange={e => setAnswer(e.target.value)} />
                <div className={'mt-3 flex gap-2'}>
                    <button
                        className={'border rounded-lg shadow p-3 hover:bg-gray-100'}
                        onClick={() => attempt(props.flashcard, answer)}>
                        Show answer
                    </button>
                    <button
                        className={'border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white'}
                        onClick={() => attempt(props.flashcard, answer)}>
                        Check answer
                    </button>
                </div>
            </div>
        </>
    )

    function attempt(flashcard, answer) {
        fetch(`${process.env.REACT_APP_API_URL}/api/flashcards/${flashcard.id}/attempt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answer: answer
            })
        })
            .then(_ => props.onAnswer())
    }
}

export default PracticeFlashcard
