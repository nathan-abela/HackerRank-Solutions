import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import { applyPolyfills, defineCustomElements } from 'h8k-components/loader';

const ARTICLES = [
    {
        title: 'Alphabet earnings',
        upvotes: 22,
        date: '2011-11-23',
    },
    {
        title: 'Artificial Mountains',
        upvotes: 200,
        date: '2019-11-23',
    },
    {
        title: 'Scaling to 100k Users',
        upvotes: 72,
        date: '2019-10-21',
    },
    {
        title: 'A message to our customers',
        upvotes: 12,
        date: '2019-10-22',
    },
    {
        title: 'the Emu War',
        upvotes: 24,
        date: '2018-04-01',
    },
    {
        title: "What's SAP",
        upvotes: 1,
        date: '2017-01-21',
    },
    {
        title: 'Simple text editor has 15k monthly users',
        upvotes: 83,
        date: '2020-02-22',
    },
];

ReactDOM.render(<App articles={ARTICLES} />, document.getElementById('root'));
registerServiceWorker();

applyPolyfills().then(() => {
    defineCustomElements(window);
});
