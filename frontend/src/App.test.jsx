import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import App from "./App";

vi.mock("axios", () => ({
  default: {
    post: vi.fn(),
  },
}));

describe("App", () => {
  it("shows a camera initialization message", () => {
    Object.defineProperty(navigator, "mediaDevices", {
      configurable: true,
      value: {
        getUserMedia: vi.fn(() => new Promise(() => {})),
      },
    });

    render(<App />);

    expect(
      screen.getByText(/starting camera/i)
    ).toBeInTheDocument();
  });
});