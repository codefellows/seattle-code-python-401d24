export default function ReportTable(props) {

    if (props.reports.length === 0) {
        return <h2 className="mt-8 text-2xl text-center text-gray-800">No Cookie Stands Available</h2>;
    }
    const headers = ['Location', ...props.hours, 'Totals'];

    return (
        <table className="w-2/3 mx-auto my-8 bg-green-300 rounded-lg">
            <HeaderRow headerValues={headers} />

            <tbody>
                {props.reports.map(report => {
                    return <ReportRow key={report.id} report={report} />;
                })}
            </tbody>

            <FooterRow reports={props.reports} />

        </table>
    );
}

function HeaderRow({ headerValues }) {
    return (
        <thead className="bg-green-500">
            <tr>
                {headerValues.map((header, index) => {
                    let className = "";
                    if (index === 0) {
                        className = "rounded-tl";
                    } else if (index === headerValues.length - 1) {
                        className = "rounded-tr";
                    }
                    return <th className={className} key={header}>{header}</th>;
                })}
            </tr>
        </thead>
    );
}

function ReportRow({ report }) {

    const total = report.hourly_sales.reduce((sum, value) => sum + value);

    const values = [report.location, ...report.hourly_sales, total];

    return (

        <tr className="odd:bg-green-400">
            {values.map((value, i) => <td className="pl-4 border border-green-900" key={i}>{value}</td>)}
        </tr>
    );
}

function FooterRow({ reports }) {

    const cellValues = ['Totals'];

    let megaTotal = 0;

    for (let i in reports[0].hourly_sales) {

        let hourlyTotal = 0;

        for (let report of reports) {
            hourlyTotal += report.hourly_sales[i];
        }

        cellValues.push(hourlyTotal);

        megaTotal += hourlyTotal;
    }

    cellValues.push(megaTotal);

    return (
        <tfoot className="bg-green-500">
            <tr>
                {cellValues.map((value, index) => {
                    let className = "border border-green-900";

                    if (index === 0) {
                        className += " rounded-bl";
                    } else if (index === cellValues.length - 1) {
                        className += " rounded-br";
                    }

                    // TODO: border is obscuring the rounding

                    return <th className={className} key={index}>{value}</th>;
                })}
            </tr>
        </tfoot>
    );
}
