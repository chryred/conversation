import 'App.scss';
import { Button } from "antd"
import PostList from "sample/PostList";

function App() {
  return (
    <div>
      Hello, React
      <Button type='primary'>Hi</Button>
      <PostList />
    </div>
  );
}

export default App;
