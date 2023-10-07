'use client'
import Image from 'next/image';
import React, { useContext, useEffect, useState } from 'react';
import toast, { Toaster } from 'react-hot-toast';
import { BsFillCloudUploadFill } from 'react-icons/bs';
import resultContext from '@/app/context/resultContext';
import { useRouter } from 'next/navigation';

const UploadForm = () => {
    const [details, setDetails] = useState({ user_name: '', images: null as null | FileList });
    const [imagePreviews, setImagePreviews] = useState<string[]>([]);
    const { images, setImages } = useContext(resultContext);
    const router = useRouter();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setDetails({ ...details, [e.target.name]: e.target.value });
    };

    const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFiles = e.target.files;

        if (selectedFiles) {
            const previews: string[] = [];

            for (let i = 0; i < selectedFiles.length; i++) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    if (e.target) {
                        previews.push(e.target.result as string);
                        if (previews.length === selectedFiles.length) {
                            setImagePreviews(previews);
                        }
                    }
                };
                reader.readAsDataURL(selectedFiles[i]);
            }

            setDetails({ ...details, images: selectedFiles });
        }
    };

    const checkValidity = () => {
        if (details.user_name.length < 3 || details.images === null) {
            toast.error('Please fill all the fields');
        } else {
            const formData = new FormData();
            formData.append('user_name', details.user_name);

            if (details.images) {
                for (let i = 0; i < details.images.length; i++) {
                    formData.append('images', details.images[i]);
                }
            }

            uploadImages(formData);
        }
    };

    const uploadImages = async (formData: FormData) => {
        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/upload`, {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();

            if (data.status === 'success') {
                toast.success('Images uploaded successfully');
                setImages({ original: data.user_images, generated: data.model_images });
            } else {
                toast.error('Something went wrong');
            }
        } catch (error: any) {
            toast.error(error.message)
        }
        setDetails({ user_name: '', images: null });
        setImagePreviews([]);
        router.push('/result');
    };

    useEffect(() => {
        console.log(images)
    }, [images])

    return (
        <>
            <Toaster />
            <div className={`min-h-screen relative pt-20 md:pt-24 pb-10 xl:pt-16 xl:pb-0 w-full flex items-center justify-center bg-cover bg-center bg-[url("https://media.istockphoto.com/id/1416628700/photo/abstract-molecular-structure.jpg?s=612x612&w=0&k=20&c=WpHSPniAsNVdj1lg1k31YUWGQkv3y2vlsiW4sOJkuXk=")]`}>
                <div className='absolute h-full inset-0 bg-gradient-to-l from-transparent via-opacity-50 to-black'></div>
                <div className="uploadContent relative z-20 w-full lg:mx-40 flex items-center justify-center space-x-8">
                    <div className='uploadForm mx-2 w-full bg-[rgba(255,255,255,0.1)] text-white flex flex-col lg:flex-row space-y-8 lg:space-y-0 rounded-xl p-4 md:p-8 backdrop-blur-2xl shadow-2xl border-[rgba(255,255,255,0.1)]'>
                        <div className="images py-10 flex items-center lg:order-2 lg:ml-8 lg:w-1/2 rounded-xl">
                            {!imagePreviews.length ? (
                                <label className='w-full cursor-pointer flex justify-center' htmlFor="uploadFile">
                                    <BsFillCloudUploadFill className='text-[20rem] text-[rgba(255,255,255,0.5)]' />
                                    <input onChange={handleFileUpload} className="hidden" type="file" name="uploadFile" id="uploadFile" multiple />
                                </label>
                            ) : (
                                <div className=" carousel rounded-box">
                                    {imagePreviews.map((preview, index) => (
                                        <div className="carousel-item w-full" key={index}>
                                            <Image src={preview} alt={`Selected Image ${index}`} width={200} height={200} className="w-full" />
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                        <div className='uploadForm py-20 lg:order-1 lg:w-1/2 bg-[rgba(255,255,255,0.1)] text-white flex flex-col rounded-xl space-y-8 p-8 backdrop-blur-2xl shadow-2xl border-[rgba(255,255,255,0.1)]'>
                            <h1 className='font-bold text-6xl'>Upload Images</h1>
                            <input onChange={handleChange} className='bg-transparent placeholder:text-white p-2 border-b-2 border-white text-white outline-none' type="text" value={details.user_name} name="user_name" id="user_name" placeholder='Enter patient name' />
                            <button onClick={checkValidity} className="btn btn-active">Upload</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default UploadForm;
