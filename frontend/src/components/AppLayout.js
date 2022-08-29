import React from "react";
// import AppHeader from "./AppHeader";
// import AppFooter from "./AppFooter";
import { Input, Menu } from "antd";
import "./AppLayout.scss";
import StoryList from "./StoryList";
import SuggestionList from "./SuggestionList";
import LogImage from "assets/logo.png";

function AppLayout(props) {
  const { children } = props;

  return (
    <div className="app">
      {/* <AppHeader /> */}
      {/* {children} */}
      {/* <AppFooter /> */}
      <div className="header">
        <h1 className="page-title">
          <img src={LogImage} alt="logo" />
        </h1>
        <div className="search">
          <Input.Search />
        </div>
        <div className="topnav">
          <Menu mode="horizontal">
            <Menu.Item>메뉴1</Menu.Item>
            <Menu.Item>메뉴2</Menu.Item>
            <Menu.Item>메뉴3</Menu.Item>
          </Menu>
        </div>
      </div>
      <div className="contents">{children}</div>
      <div className="sidebar">
        <StoryList style={{ marginBottom: "1rem" }} />
        <SuggestionList />
      </div>
      <div className="footer">&copy; 2022.08 conversation</div>
    </div>
  );
}

export default AppLayout;
