import { Layout } from "antd"
import React from "react";
import "./AppRightSider.scss";
import StoryList from "../story/StoryList";
import SuggestionList from "../suggestion/SuggestionList";


const { Sider } = Layout;
const AppRightSider = () => {
    return (
        <Sider className="right-sider"
            theme="light"
        >
            <StoryList style={{ marginBottom: "1rem" }} />
            <SuggestionList />
        </Sider>
    );
};

export default AppRightSider;