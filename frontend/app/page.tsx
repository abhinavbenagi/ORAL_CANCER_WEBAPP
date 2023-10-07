'use client'
import { useRouter } from "next/navigation";
import UploadForm from "./components/upload/UploadForm";
import { useEffect, useState } from "react";

export default function Home() {

  const [loggedIn, setLoggedIn] = useState(false);
  const router = useRouter();

  const handleRedirection = async () => {
    const formData = new FormData();
    const username = localStorage.getItem("username");
    const password = localStorage.getItem("password");

    if (username && password) {
      formData.append('username', username);
      formData.append('password', password);

      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();

      if (data.status === 'success') {
        setLoggedIn(true);
      } else {
        router.push('/sign-in');
      }
    } else {
      router.push('/sign-in');
    }
  }


  useEffect(() => {
    handleRedirection();
  }, [])

  return (
    <>
      {loggedIn && <UploadForm />}
    </>
  )
}
