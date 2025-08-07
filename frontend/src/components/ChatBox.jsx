import React, { useState } from "react";
import { askQuestion } from "../api/client";

const ChatBox = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await askQuestion(question);
    setAnswer(res.answer);
  };

  return (
   <div className="glass-container">
      <form onSubmit={handleSubmit}>
        <input
          className="glass-input"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me anything"
        />
        <button type="submit" className="glass-button">Ask</button>
      </form>
      {answer && (
        <div style={{ whiteSpace: "pre-wrap", marginTop: "1rem" }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
    )}
   </div>
  );
};

export default ChatBox;
