// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/react_basic
// Difficulty: Basic
// Language: JavaScript - React

// ========================
//         Solution
// ========================

import React, { useState } from 'react';

function Slides({ slides }) {
    const [activeSlideIdx, setActiveSlideIdx] = useState(0);
    const [disabled, setDisabled] = useState({
        prev: true,
        next: false,
        restart: true,
    });

    const onClickNext = () => {
        var curSlideIdx = activeSlideIdx;

        if (curSlideIdx < slides.length - 1) {
            curSlideIdx++;
            setActiveSlideIdx(curSlideIdx);
            setDisabled({
                ...disabled,
                prev: false,
                restart: false,
            });
        }

        if (curSlideIdx === slides.length - 1) {
            setDisabled({
                ...disabled,
                next: true,
            });
        }
    };

    const onClickPrev = () => {
        var curSlideIdx = activeSlideIdx;

        if (curSlideIdx > 0) {
            curSlideIdx--;
            setActiveSlideIdx(curSlideIdx);
            setDisabled({
                ...disabled,
                next: false,
            });
        }

        if (curSlideIdx === 0) {
            setDisabled({
                ...disabled,
                prev: true,
                restart: true,
            });
        }
    };

    const onClickRestart = () => {
        setActiveSlideIdx(0);
        setDisabled({
            ...disabled,
            prev: true,
            next: false,
            restart: true,
        });
    };

    return (
        <div>
            <div id='navigation' className='text-center'>
                <button
                    data-testid='button-restart'
                    className='small outlined'
                    onClick={() => onClickRestart()}
                    disabled={disabled.restart}
                >
                    Restart
                </button>
                <button
                    data-testid='button-prev'
                    className='small'
                    onClick={() => onClickPrev()}
                    disabled={disabled.prev}
                >
                    Prev
                </button>
                <button
                    data-testid='button-next'
                    className='small'
                    onClick={() => onClickNext()}
                    disabled={disabled.next}
                >
                    Next
                </button>
            </div>
            <div id='slide' className='card text-center'>
                <h1 data-testid='title'>{slides[activeSlideIdx].title}</h1>
                <p data-testid='text'>{slides[activeSlideIdx].text}</p>
            </div>
        </div>
    );
}

export default Slides;
