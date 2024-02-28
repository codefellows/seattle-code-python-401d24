import Link from 'next/link';

export default function Header() {
    return (
      <header className="flex items-center justify-between p-4 text-gray-800 bg-green-500">
      <h1 className="text-4xl">Cookie Stand Admin</h1>
      <nav>
          <Link href="/overview" className="px-2 py-1 rounded bg-green-50">Overview</Link>
      </nav>
  </header>
    );
}
