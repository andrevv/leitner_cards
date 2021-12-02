import {useCallback, useEffect, useMemo, useRef, useState} from 'react'
import PracticeFlashcard from './PracticeFlashcard'

function Practice(props) {
    const [flashcards, setFlashcards] = useState([])
    const [index, setIndex] = useState(0)
    const [current, setCurrent] = useState()

    useEffect(() => {
        fetch('/api/flashcards')
            .then(resp => resp.json())
            .then(data => {
                setFlashcards(data)
                setIndex(0)
            })
    }, [])

    return (
        <>
            <div className={'container flex justify-center pt-24'}>
                <div>
                    {index < flashcards.length &&
                        <PracticeFlashcard
                            flashcard={flashcards[index]}
                            onAnswer={onAnswer} />
                    }
                    {index === flashcards.length &&
                        <h1 className={'text-3xl'}>All done!</h1>
                    }
                </div>
            </div>
        </>
    )

    function onAnswer() {
        setCurrent(flashcards[index])
        setIndex(index + 1)
    }
}

export default Practice
