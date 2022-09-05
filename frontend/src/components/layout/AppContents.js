import { Layout } from "antd";
import React from "react";
import "./AppContents.scss";

const { Content } = Layout;

const AppContent = ({ contents }) => {
    return (
        <Content className="contents">
            {contents}
        </Content>
    )

};

export default AppContent;