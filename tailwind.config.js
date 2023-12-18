/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./portfolio/**/*.{html,js}"],
  darkMode: "class",
  theme: {
    fontFamily: {
      merriweather: ['Merriweather', 'serif'],
    },
    extend: {
      backgroundImage: {
        'matrix-pattern': "url('./background.png')",
        'sun': "url('./sun.jpeg')",
        'moon': "url('./moon.jpeg')",
      },
      colors: {
        portPurple: '#2D1250',
        portYellow: '#FFC857',
      },
      animation: {
        moon: 'moonGrow 0.2s linear 0.2s',
        sun: 'sunGrow 0.2s linear 0.2s',

    },
      keyframes: {
        moonGrow: {
          '0%': { backgroundSize: '40px 40px' },
          '50%': { backgroundSize: '38px 38px' },
          '100%': { backgroundSize: '40px 40px' },
        },
        sunGrow: {
          '0%': { backgroundSize: '40px 40px' },
          '50%': { backgroundSize: '38px 38px' },
          '100%': { backgroundSize: '40px 40px' },
        },
        },
  },
  plugins: [],
}
}