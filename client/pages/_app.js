import "../styles/globals.css";
// import BackgroundVideo from "./pages/backgroundvideo.js";

function MyApp({ Component, pageProps }) {
  return (
    <>
      {/* <BackgroundVideo /> */}
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
