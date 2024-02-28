export default function CreateForm(props) {

    function handleSubmit(event) {
        event.preventDefault();
        props.onCreate({
            id: event.target.location.value,
            location: event.target.location.value,
            minimumCustomersPerHour: parseInt(event.target.minimumCustomersPerHour.value),
            maximumCustomersPerHour: parseInt(event.target.maximumCustomersPerHour.value),
            averageCookiesPerSale: parseFloat(event.target.averageCookiesPerSale.value),
            hourly_sales: [48, 42, 30, 24, 42, 24, 36, 42, 42, 48, 36, 42, 24, 36],

        });
        event.target.reset();
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="flex flex-col w-2/3 gap-2 p-4 mx-auto bg-green-300 border-green-500 rounded-lg" >

            <legend className="text-2xl text-center">Create Cookie Stand</legend>

            <div className="flex py-4">
                <label className="mr-2" htmlFor="location">Location</label>
                <input className="flex-auto pl-2 placeholder-gray-50" type="text" name="location" />
            </div>

            <div className="flex gap-2 text-center item-centereduce">

                <fieldset className="flex flex-col flex-1 min-w-0 p-2 ">
                    <label htmlFor="minimumCustomersPerHour">Minimum Customers per Hour</label>
                    <input className="pl-2" type="number" name="minimumCustomersPerHour" />
                </fieldset>

                <fieldset className="flex flex-col flex-1 min-w-0 p-2 ">
                    <label htmlFor="maximumCustomersPerHour">Maximum Customers per Hour</label>
                    <input className="pl-2" type="number" name="maximumCustomersPerHour" />
                </fieldset>

                <fieldset className="flex flex-col flex-1 min-w-0 p-2 ">
                    <label htmlFor="averageCookiesPerSale">Average Cookies per Sale</label>
                    <input className="pl-2" type="number" name="averageCookiesPerSale" step=".1" />
                </fieldset>
                <button type="submit" className="flex-1 min-w-0 bg-green-500">Create</button>
            </div>

        </form>
    );
}
