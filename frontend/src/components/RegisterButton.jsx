import { useNavigate } from "react-router-dom";

function RegisterButton({ children = "Login" }) {
    const nav = useNavigate();

    return (
        <button onClick={() => nav("/register")}>
            {children}
        </button>
    );
}
export default RegisterButton;
