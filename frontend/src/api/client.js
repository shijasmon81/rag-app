import axios from "axios";

// export const askQuestion = async (question) => {
//   const res = await axios.post(
//     "http://localhost:8000/ask",
//     { question }, // send as JSON
//     {
//       headers: {
//         "Content-Type": "application/json",
//       },
//     }
//   );
//   return res.data;
// };

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export const askQuestion = async (question) => {
  const res = await fetch(`${BACKEND_URL}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });
  return await res.json();
};
