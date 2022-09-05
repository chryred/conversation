import React from "react";
import "./AppHeader.scss";
import { Input, Menu, Layout } from "antd";
import LogImage from "assets/logo.png";

const { Header } = Layout;
function AppHeader() {
    return (
        <Header className="header">
            <img src={LogImage} alt="logo" />
            <div className="search">
                <Input.Search />
            </div>
            <div>
                <Menu className="topnav" mode="horizontal">
                    <Menu.Item>메뉴1</Menu.Item>
                    <Menu.Item>메뉴2</Menu.Item>
                    <Menu.Item>메뉴3</Menu.Item>
                </Menu>
            </div>
        </Header>
    )
}

export default AppHeader;