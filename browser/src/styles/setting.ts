export function toggleTheme(theme: string | null) {
  if (!theme) {
    document.documentElement.setAttribute('data-theme', "dark");
    return
  }
  document.documentElement.setAttribute('data-theme', theme);
}