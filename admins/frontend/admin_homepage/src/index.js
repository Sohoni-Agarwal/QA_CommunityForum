import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import {Provider} from 'react-redux';
import {BrowserRouter} from 'react-router-dom';

import App from './App/index';
import * as serviceWorker from './serviceWorker';
import reducer from './store/reducer';
import config from './config';


import { ApolloClient, InMemoryCache } from 'apollo-client-preset';
import { setContext } from 'apollo-link-context';
import { createHttpLink } from 'apollo-link-http';
import { ApolloProvider } from 'react-apollo';

export const store = createStore(reducer);

const authLink = setContext((_, {
  headers
}) => {
  const token = localStorage.getItem('authToken');
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : ''
    }
  };
});
const httpLink = createHttpLink({
  uri: 'http://localhost:1138/graphql'
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
});

const Main = () => (
  <ApolloProvider client={client}>
    <Provider store={store}>
      <BrowserRouter basename={config.basename}>
            {/* basename="/datta-able" */}
            <App />
        </BrowserRouter>
    </Provider>
  </ApolloProvider>
);

ReactDOM.render(<Main />, document.body);
/*
const store = createStore(reducer);

const app = (
    <Provider store={store}>
        <BrowserRouter basename={config.basename}>
            {/* basename="/datta-able" }
            <App />
        </BrowserRouter>
    </Provider>
);

ReactDOM.render(app, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA

*/
serviceWorker.unregister();
