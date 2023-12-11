/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./portfolio/**/*.{html,js}"],
  theme: {
    fontFamily: {
      merriweather: ['Merriweather', 'serif'],
    },
    extend: {
      backgroundImage: {
        'matrix-pattern': "url('./background.png')",
      },
    },
  },
  plugins: [],
}

