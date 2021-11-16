import {useCallback, useEffect, useMemo, useRef, useState} from 'react'
import PracticeFlashcard from './PracticeFlashcard'

function Practice(props) {
    const [flashcards, setFlashcards] = useState([])
    const [current, setCurrent] = useState()

    const it = useMemo(() => {
        const iter = gen(flashcards)
        setCurrent(iter.next().value)
        return iter
    }, [flashcards])

    return (
        <>
            <button
                className={'border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2'}
                onClick={getFlashcards}>
                Start practicing
            </button>
            <div className={'container flex justify-center'}>
                <div>
                    {current &&
                        <PracticeFlashcard
                            flashcard={current}
                            onAnswer={onAnswer} />}
                </div>
            </div>
        </>
    )

    function getFlashcards() {
        fetch('http://localhost:5000/api/flashcards')
            .then(resp => resp.json())
            .then(data => {
                setFlashcards(data)
            })
    }

    function onAnswer() {
        setCurrent(it.next().value)
    }

    function* gen(arr) {
        yield* arr
    }
}

export default Practice
