import React from "react";
import AppHeader from "./AppHeader";
import AppFooter from "./AppFooter";
import "./AppLayout.scss";
import StoryList from "./StoryList";
import SuggestionList from "./SuggestionList";

function AppLayout(props) {
  const { children } = props;

  return (
    <div className="app">
      <AppHeader />
      {/* <AppFooter /> */}
      <div className="contents">{children}</div>
      <div className="sidebar">
        <StoryList style={{ marginBottom: "1rem" }} />
        <SuggestionList />
      </div>
      <AppFooter />
    </div>
  );
}

export default AppLayout;
