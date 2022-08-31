import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Axios from "axios";
import { Form, Input, Button, notification, Descriptions } from "antd"
import { SmileOutlined, FrownOutlined } from "@ant-design/icons";


const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};

const tailLayout = {
    wrapperCol: { offset: 8, span: 16 },
}

function Signup() {
    const navigate = useNavigate();
    const [fieldErrors, setFieldErrors] = useState({});

    const onFinish = (values) => {
        console.log('Success:', values);
        async function awaitSignup() {
            const { username, password } = values;
            setFieldErrors({});

            const data = { username, password };
            try {
                const response = await Axios.post("http://localhost:8000/accounts/signup/", data);
                notification.open({
                    message: "회원가입 성공",
                    description: "로그인 페이지로 이동합니다.",
                    icon: <SmileOutlined style={{ color: "#108ee9" }} />
                });

                navigate("/accounts/login");
            }
            catch (error) {
                notification.open({
                    message: "회원가입 실패",
                    description: "아이디/암호를 확인해주세요.",
                    icon: <FrownOutlined style={{ color: "#ff3333" }} />
                });

                if (error.response) {
                    console.log(error.response);
                    const { data: fieldErrorMessages } = error.response;
                    setFieldErrors(
                        Object.entries(fieldErrorMessages).reduce((acc, [fieldName, errors]) => {
                            // errors: ["m1", "m2"]
                            acc[fieldName] = {
                                validateStatus: "error",
                                help: errors.join(" ")
                            };
                            return acc;
                        }, {})
                    );
                }
            }
        }

        awaitSignup();
    };

    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };

    return (
        <Form
            {...layout}
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
            autoComplete="off"
        >
            <Form.Item
                label="Username"
                name="username"
                rules={[
                    { required: true, message: 'Please input your username!', },
                    { min: 5, message: "5글자 이상 입력해주세요." },
                ]}
                hasFeedback
                {...fieldErrors.username}
            >
                <Input />
            </Form.Item>

            <Form.Item
                label="Password"
                name="password"
                rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                ]}
                {...fieldErrors.password}
            >
                <Input.Password />
            </Form.Item>

            <Form.Item
                name="remember"
                valuePropName="checked"
                wrapperCol={{
                    offset: 8,
                    span: 16,
                }}
            >
            </Form.Item>

            <Form.Item
                {...tailLayout}
            >
                <Button type="primary" htmlType="submit">
                    Submit
                </Button>
            </Form.Item>
        </Form>
    );
}

export default Signup;