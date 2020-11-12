// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/react_basic
// Difficulty: Basic
// Language: JavaScript - React

// ========================
//         Solution
// ========================

import React, { useState, useEffect } from 'react';
import './App.css';
import 'h8k-components';

import Articles from './components/Articles';

const title = 'Sorting Articles';

function App({ articles }) {
    const [articleList, setArticleList] = useState(articles);

    useEffect(() => {
        sortBy('upvotes');
    }, []);

    function upVotes(a, b) {
        if (a.upvotes > b.upvotes) {
            return -1;
        }
        if (a.upvotes < b.upvotes) {
            return 1;
        }
        return 0;
    }

    function dates(a, b) {
        const aDate = new Date(a.date);
        const bDate = new Date(b.date);
        if (aDate > bDate) {
            return -1;
        }
        if (aDate < bDate) {
            return 1;
        }
        return 0;
    }

    const sortBy = (type) => {
        var newArticles = [];
        Object.assign(newArticles, articleList);

        if (type === 'upvotes') {
            newArticles.sort(upVotes);
        } else if (type === 'dates') {
            newArticles.sort(dates);
        }
        setArticleList(newArticles);
    };

    return (
        <div className='App'>
            <h8k-navbar header={title}></h8k-navbar>
            <div className='layout-row align-items-center justify-content-center my-20 navigation'>
                <label className='form-hint mb-0 text-uppercase font-weight-light'>
                    Sort By
                </label>
                <button
                    data-testid='most-upvoted-link'
                    className='small'
                    onClick={() => sortBy('upvotes')}
                >
                    Most Upvoted
                </button>
                <button
                    data-testid='most-recent-link'
                    className='small'
                    onClick={() => sortBy('dates')}
                >
                    Most Recent
                </button>
            </div>
            <Articles articles={articleList} />
        </div>
    );
}

export default App;
