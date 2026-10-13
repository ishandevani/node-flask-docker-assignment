const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;
const BACKEND_URL =
    process.env.BACKEND_URL || "http://localhost:5000";

app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());

app.post("/api/user", async (req, res) => {
    try {
        const response = await fetch(
            `${BACKEND_URL}/user`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(req.body),
                signal: AbortSignal.timeout(10000)
            }
        );

        const result = await response.json();
        res.status(response.status).json(result);
    } catch (error) {
        console.error("Backend request failed:", error.message);

        res.status(502).json({
            message: "Unable to communicate with the Flask backend."
        });
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Frontend running on port ${PORT}`);
});