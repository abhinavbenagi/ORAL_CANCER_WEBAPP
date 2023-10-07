'use client'
import React, { useContext } from 'react'
import resultContext from '@/app/context/resultContext'

const Display = () => {

    const { images } = useContext(resultContext)

    return (
        <div className="result flex flex-col items-center justify-center">
            <div className="heading w-full px-10">
                <h1 className='text-8xl py-10 font-bold'>Results</h1>
            </div>
            <div className="wrapper px-5 lg:px-10 flex flex-col lg:flex-row space-y-4 lg:space-y-0 lg:space-x-4 w-full">
                <div className="lg:w-1/2 carousel rounded-box shadow-2xl shadow-black transition-all duration-300">
                    {
                        images.original && images.original.map((array, index) => (
                            <div key={index} className="result__image carousel-item w-full">
                                <img src={`${process.env.NEXT_PUBLIC_API_URL}/uploads/${array[0]}.jpg`} alt="result" />
                            </div>
                        ))
                    }
                </div>
                <div className="lg:w-1/2 carousel rounded-box shadow-2xl shadow-black transition-all duration-300">
                    {
                        images.generated && images.generated.map((array, index) => (
                            <div key={index} className="result__image carousel-item w-full">
                                <img src={`${process.env.NEXT_PUBLIC_API_URL}/generated/${array[0]}.jpg`} alt="result" />
                            </div>
                        ))
                    }
                </div>
            </div>
        </div>
    )
}

export default Display
