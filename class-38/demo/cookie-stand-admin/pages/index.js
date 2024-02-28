import Head from 'next/head';
import { useState } from 'react';
import Header from '@/components/header';
import Footer from '@/components/footer';
import ReportTable from '@/components/report-table';
import CreateForm from '@/components/create-form';
import { hours } from '../data';

export default function Home() {

    // const [standData, setStandData] = useState({location:"coming soon"});
    const [standReports, setStandReports] = useState([]);

    function handleCreate(standInfo) {
        setStandReports([...standReports, standInfo]);
    }

    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <main className="p-8">
                <CreateForm onCreate={handleCreate} />
                <ReportTable reports={standReports} hours={hours} />
            </main>
            <Footer />
        </div>
    );
}








