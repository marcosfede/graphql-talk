import React from "react"
import { graphql } from "react-apollo"
import gql from "graphql-tag"

const User = ({ match }) => {
  return <div>user: {match.params.id}</div>
}

const USER_QUERY = gql`
  {
    users {
      id
      name
      lastName
      posts {
        title
      }
      comments {
        text
      }
    }
  }
`
export default graphql(USER_QUERY)(User)
