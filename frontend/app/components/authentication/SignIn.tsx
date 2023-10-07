'use client'
import React, { useState } from 'react'
import { FaEnvelope, FaLock } from 'react-icons/fa'
import toast, { Toaster } from 'react-hot-toast';
import Link from 'next/link';
import { useRouter } from 'next/navigation'

const SignIn = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' })
    const router = useRouter()

    const onChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
        setCredentials({ ...credentials, [e.target.name]: e.target.value })
    }

    const checkValidity = (e: React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault()
        if (credentials.username === '' || credentials.password === '') {
            toast.error('Please fill all the fields')
        } else if (credentials.password.length < 8) {
            toast.error('Password must be atleast 8 characters long')
        }
        else {
            handleSignIn()
        }
    }

    const handleSignIn = async () => {
        const formData = new FormData();
        formData.append('username', credentials.username);
        formData.append('password', credentials.password);

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login`, {
            method: 'POST',
            body: formData
        });
        const data = await res.json()

        if (data.status === 'success') {
            toast.success('Logged in successfully');
            localStorage.setItem('username', credentials.username);
            localStorage.setItem('password', credentials.password);
            router.push('/');
        } else {
            toast.error('Something went wrong');
        }
        setCredentials({ username: '', password: '' })
    }


    return (
        <>
            <Toaster />
            <div className={`wrapper transition-all px-5 lg:px-0 duration-300 h-screen font-jost bg-gray-200 flex justify-center items-center`}>
                <div className="content w-full md:w-1/2 lg:w-[27%] border bg-pureWhite border-gray-300 p-6 rounded-2xl shadow-2xl shadow-black">
                    <div className="heading py-4">
                        <h1 className='bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500 text-2xl font-jost'>Sign in</h1>
                        <h3>to continue to dashboard</h3>
                    </div>
                    <form className='form flex w-full flex-col'>
                        <div className="username flex items-center mb-2 px-2 py-1 border-2 border-gray-300 rounded-xl">
                            <FaEnvelope className='text-gray-500 pl-1' />
                            <input onChange={onChangeHandler} className='text-base w-full pl-4 p-2 outline-none text-gray-500 bg-pureWhite ' placeholder='Enter your username' value={credentials.username} type="text" name="username" id="username" />
                        </div>
                        <div className="password flex items-center mb-2 px-2 py-1 border-2 border-gray-300 rounded-xl">
                            <FaLock className='text-gray-500 pl-1' />
                            <input onChange={onChangeHandler} className='text-base w-full pl-4 p-2 outline-none text-gray-500 bg-pureWhite ' placeholder='Enter the password' value={credentials.password} type="password" name="password" id="password" />
                        </div>
                        <div className="forgotPassword flex items-center space-x-1 justify-center text-sm">
                            <Link href='/sign-in' className='text-[#FE538D]'>Forgot Password?</Link>
                        </div>
                        <button onClick={checkValidity} className='py-2 my-5 w-1/2 mx-auto hover:-translate-y-[0.1rem] text-white  bg-[#FE538D] duration-150 font-jost font-semibold border rounded-md px-3 hover:shadow-2xl shadow-black border-[rgba(255,255,255,0.1)]'>Sign In</button>
                    </form>
                    <div className='horizontalRule mx-auto h-[0.1rem] relative mb-4 w-[30%] bg-[#FE538D]'></div>
                    <div className="login flex items-center space-x-1 justify-center text-sm">
                        <span>No account?</span> <Link href='/sign-up' className='text-[#FE538D]'>Sign Up</Link>
                    </div>
                </div>


            </div>
        </>
    )
}

export default SignIn
