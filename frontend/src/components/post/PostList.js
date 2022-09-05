import React, { useEffect, useState } from "react";
import Axios from "axios";
import Post from "./Post";

const apiUrl = "http://localhost:8000/api/posts/";

function PostList() {
  const [postList, setPostList] = useState([]);

  useEffect(() => {
    Axios.get(apiUrl)
      .then((response) => {
        const { data } = response;
        // console.log("loaded response :", response);
        setPostList(data);
      }) // 에러코드 400미만일 경우
      .catch((error) => {
        console.log(error.response);
      });
  }, []);
  return (
    <div>
      {postList.map((post) => {
        return <Post key={post.id} post={post} />;
      })}
    </div>
  );
}

export default PostList;
