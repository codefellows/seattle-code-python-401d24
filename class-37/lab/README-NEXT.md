# Next.js Projects

Next.js projects obviously have a different creation/submission flow than Python project.

## Project Creation

- Base project off [Next + Tailwind Template](https://github.com/vercel/next.js/tree/canary/examples/with-tailwindcss)
- > `npx create-next-app@latest --js --no-app`
- name your project, e.g. your-awesome-project.
- accept defaults for remaining options.
- > cd your-awesome-project
- > npm run dev
- Strip out un-needed template code and assets.
- Update included README.md.
- Note: create-next-app will create a git repository for you.
- You will connect your local repo with Github in next step.

## Repositories

### On Github site

- create **EMPTY** repository e.g. `your-awesome-project` on Github.
  - **Do NOT** initialize with README, license or gitignore.
  - Those will be added soon
- The next screen will have a "…or push an existing repository from the command line" section with some commands available to copy. Copy them ;)

### On local system

- Navigate terminal to root of project.
- **IMPORTANT** Make sure your local git status is `nothing to commit, working tree clean`.
  - Do an add/commit as needed to make it so.
- Paste the copied commands into terminal.
- Will look something like below

```bash
git remote add origin https://github.com/Awesome-Dev/your-awesome-project.git
git branch -M main
git push -u origin main
```

Now everything is wired up between local machine and Github.

If you run into issues grab a TA.
