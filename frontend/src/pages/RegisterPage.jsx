export default function RegisterPage() {
    return (
        <div>
            <h1> Register </h1>
            <form>
                <input placeholder="email" type="email" />
                <input placeholder="username" />
                <input placeholder="password" type="password"/>
                <button type="submit">Create Account</button>
            </form>
        </div>
    );
}
