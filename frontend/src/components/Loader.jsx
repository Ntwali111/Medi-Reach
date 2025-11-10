import { Loader2 } from 'lucide-react';

const Loader = ({ size = 'medium', fullScreen = false }) => {
  const sizeClasses = {
    small: 'w-4 h-4',
    medium: 'w-8 h-8',
    large: 'w-12 h-12',
  };

  const loader = (
    <div className="flex items-center justify-center">
      <Loader2 
        className={`${sizeClasses[size]} text-primary animate-spin`} 
      />
    </div>
  );

  if (fullScreen) {
    return (
      <div className="fixed inset-0 bg-white/80 backdrop-blur-sm flex items-center justify-center z-50">
        <div className="text-center">
          <Loader2 className="w-16 h-16 text-primary animate-spin mx-auto" />
          <p className="mt-4 text-secondary font-medium">Loading...</p>
        </div>
      </div>
    );
  }

  return loader;
};

export default Loader;
