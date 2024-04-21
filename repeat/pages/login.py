"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx
from repeat.state.auth import AuthState


def login():
    """The login page."""
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                rx.image(src="/login/login_top.svg", margin_bottom="1em"),
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    height="50px",
                    width="400px",
                    border_radius="8px",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    height="50px",
                    width="400px",
                    border_radius="8px",
                ),
                rx.link(
                    rx.image(src="/login/login_button.svg", 
                    margin_top="1em",),
                    on_click=AuthState.login,
                ),
                rx.image(src="/login/google_button.svg"),
                spacing="5",
                text_align="center",
                width="100%",
            ),
            align_items="center",
            justify_content="center",
            background="rgba(255,255,255,0.08)",
            border="1px solid rgba(255,255,255,0.2)",
            padding="3em",
            width="500px",
            border_radius="20px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup"),
            color="gray",
        ),
        background_image="url('/background.svg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        height="100vh",
        width="100vw",
        display="flex",
        justify_content="center",
        align_items="center",
    )