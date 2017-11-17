import React from "react"
import ReactDOM from "react-dom"
import "./index.css"
import App from "./App"
import User from "./User"
import Post from "./Post"
import { InMemoryCache } from "apollo-cache-inmemory"
import { HttpLink } from "apollo-link-http"
import { ApolloProvider } from "react-apollo"
import { ApolloClient } from "apollo-client"
import { BrowserRouter as Router, Route } from "react-router-dom"

const client = new ApolloClient({
  link: new HttpLink({
    uri: "http://localhost:8000/graphql/"
  }),
  cache: new InMemoryCache()
})

ReactDOM.render(
  <ApolloProvider client={client}>
    <Router>
      <div>
        <Route exact path="/" component={App} />
        <Route path="/post/:id" component={Post} />
        <Route path="/user/:id" component={User} />
      </div>
    </Router>
  </ApolloProvider>,
  document.getElementById("root")
)
