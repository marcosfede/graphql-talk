## simple query 
```
query {
  users {
    name
    lastName
    posts {
      title
    }
  }
}
```

## deeper query 
```
query {
  users {
    id
    name
    lastName
    posts {
      title
      content
      comments {
        text
      }
    }
    comments {
      text
      post {
        title
      }
    }
  }
}
```

## example mutation create comment
```
mutation {
  createComment(text: "este es un comentario", post: 1, user: 2) {
    ok
    comment {
      text
      post {
        title
        content
      }
      user {
        name
        lastName
      }
    }
  }
}
```

## verify it has been saved
```
{
	comments {
    text
    user {
      name
      lastName
    }
  }
}
```


