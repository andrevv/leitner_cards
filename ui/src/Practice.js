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

    useEffect(() => {
        fetch('http://localhost:5000/api/flashcards')
            .then(resp => resp.json())
            .then(data => {
                setFlashcards(data)
            })
    }, [])

    return (
        <>
            <div className={'container flex justify-center pt-24'}>
                <div>
                    {current &&
                        <PracticeFlashcard
                            flashcard={current}
                            onAnswer={onAnswer} />}
                </div>
            </div>
        </>
    )

    function onAnswer() {
        setCurrent(it.next().value)
    }

    function* gen(arr) {
        yield* arr
    }
}

export default Practice
