import React from "react";
import AppHeader from "./AppHeader";
import AppMenuSider from "./AppMenuSider";
import AppContents from "./AppContents";
import AppRightSider from "./AppRightSider";
import AppFooter from "./AppFooter";
import "./AppLayout.scss";
import { Layout } from "antd";

function AppLayout(props) {
  const { children } = props;

  return (
    <Layout>
      <AppHeader />
      <Layout className="layout">
        <AppMenuSider />
        <AppContents contents={children} />
        <AppRightSider />
      </Layout>
      <AppFooter />
    </Layout>
  );
}

export default AppLayout;
