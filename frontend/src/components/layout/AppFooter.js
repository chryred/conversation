import React from "react";
import "./AppFooter.scss";
import { Layout, Breadcrumb } from "antd";
const { Footer } = Layout;
function AppFooter() {
    return (
        <Footer className="footer">
            <Breadcrumb className="crumb">
                <Breadcrumb.Item>Home</Breadcrumb.Item>
                <Breadcrumb.Item>List</Breadcrumb.Item>
                <Breadcrumb.Item>App</Breadcrumb.Item>
            </Breadcrumb>
            &copy; 2022.08 conversation
        </Footer>
    )
}

export default AppFooter;