import { useRouter } from "next/router";
import Link from "next/link";

export default function Navbar() {
  const router = useRouter();

  const isHomeGridPage = router.pathname === "/homegrid";

  const navbarStyle = {
    backgroundColor: isHomeGridPage ? "white" : "black",
    color: isHomeGridPage ? "black" : "white",
    // Add your other styles here
  };

  return (
    <nav style={navbarStyle}>
      <ul>
        <li>
          <Link href="/">Home</Link>
        </li>
        {/* <li>
          <Link href="/baselayer">Baselayer</Link>
        </li> */}
        <li>
          <Link href="/destination">Destination</Link>
        </li>
        <li>
          <Link href="/signup">Signup</Link>
        </li>
        <li>
          <Link href="/user-landing-page">User Landing Page</Link>
        </li>
      </ul>
    </nav>
  );
};


