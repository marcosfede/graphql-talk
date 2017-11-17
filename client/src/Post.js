import React from "react"
import { graphql } from "react-apollo"
import gql from "graphql-tag"

const Post = ({ match }) => {
  return <div>post: {match.params.id}</div>
}

const POST_QUERY = gql`
  {
    posts {
      id
      title
      content
      author {
        name
      }
      comments {
        text
      }
    }
  }
`
export default graphql(POST_QUERY)(Post)
