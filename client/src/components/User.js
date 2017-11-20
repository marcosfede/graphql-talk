import React from "react"
import { graphql } from "react-apollo"
import gql from "graphql-tag"
import './User.css'
import {Row, Col} from 'antd'

 
const User = ({ match, data }) => {
  const { user, loading, error } = data
  if (error) return error
  if (loading) return <div>loading...</div>
  return (
    <div className="user-container">
      <div className="user-wrp">
        <div className="user-header">User:</div>
        <div className="user-name">
          {user.name} {user.lastName}
        </div>
      </div>
      <Row>
        <Col span={12}>
      <div className="comments-container">
        <div className="comments-header">
          {user.name} {user.lastName} latest comments:
        </div>
        {user.comments.map(comment => (
          <div className="comment" key={comment.id}>"{comment.text}" on {comment.post.author.name} {comment.post.author.lastName}'s post</div>
        ))}
      </div>
      </Col>
      <Col span={12}>
      <div className="posts-container">
        <div className="post-header">
          {user.name} {user.lastName} latest posts:
        </div>
        {user.posts.map(post => <div className="post" key={post.id}>{post.title}</div>)}
      </div>
      </Col>
      </Row>
    </div>
  )
}

const USER_QUERY = gql`
  query userById($id: Int!) {
    user(id: $id) {
      id
      name
      lastName
      posts {
        id
        title
      }
      comments {
        id
        text
        post {
          id
          author {
            id
            name
            lastName
          }
        }
      }
    }
  }
`
export default graphql(USER_QUERY, {
  options: ({ match }) => {
    return { variables: { id: match.params.id } }
  }
})(User)
